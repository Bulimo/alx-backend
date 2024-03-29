import redis from 'redis';

const publisher = redis.createClient();

publisher.on('connect', () => {
  console.log('Redis client connected to the server');
});

publisher.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});

const channel = 'holberton school channel';

function publishMessage(message, time) {
  setTimeout(() => {
    console.log(`About to send "${message}"`);
    publisher.publish(channel, message);
  }, time);
}

// Call the publishMessage function with different messages and times
publishMessage('Holberton Student #1 starts course', 100);
publishMessage('Holberton Student #2 starts course', 200);
publishMessage('KILL_SERVER', 300);
publishMessage('Holberton Student #3 starts course', 400);
