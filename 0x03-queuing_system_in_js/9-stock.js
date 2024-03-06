const redis = require('redis');
const { promisify } = require('util');
const express = require('express');

const listProducts = [
  { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
  { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
  { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
  { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 },
];

// redis client
const client = redis.createClient();
client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// --- express app ---
const app = express();
const hostname = 'localhost';
const port = 1245;

app.use(express.json());

app.listen(port, () => {
  console.log(`API available on ${hostname} port ${port}`);
});

// functions
const getItemById = (id) => listProducts.find((item) => item.itemId === id);

const reserveStockById = (itemId, stock) => {
  client.set(`item.${itemId}`, stock, redis.print);
};

const getCurrentReservedStockById = async (itemId) => {
  const getAsync = promisify(client.get).bind(client);
  const item = await getAsync(`item.${itemId}`);
  return item;
};

// routes
app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
  const id = parseInt(req.params.itemId, 10);
  const item = getItemById(id);
  if (!item) return res.json({ status: 'Product not found' });

  const currentStock = await getCurrentReservedStockById(id);
  const stock = currentStock !== null ? currentStock : item.initialAvailableQuantity;
  item.currentQuantity = stock;
  return res.json(item)

});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const item = getItemById(itemId);

  if (!item) return res.json({ status: 'Product not found' });

  let currentStock = await getCurrentReservedStockById(itemId);
  if (currentStock === null) currentStock = item.initialAvailableQuantity;

  if (currentStock <= 0) return res.json({ status: 'Not enough stock available', itemId: item.Id });

  reserveStockById(itemId, parseInt(currentStock, 10) - 1);
  return res.json({ status: 'Reservation confirmed', itemId: item.itemId });
});

module.exports = app;
