import kue from 'kue';
const queue = kue.createQueue();

const job = queue.create('push_notification_code', {
  phoneNumber: '0712345678',
  message: 'Your account balance is 50%',
}).save((err) => {
  if (!err) console.log(`Notification job created: ${job.id}`);
});

job.on('complete', () => {
  console.log('Notification job completed');
}).on('failed', () => {
  console.log('Notification job failed');
});
