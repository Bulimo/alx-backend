import kue from 'kue';
const queue = kue.createQueue();

const sendNotification = (phoneNumber, message) => {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

// Queue process for push_notification_code jobs
queue.process('push_notification_code', (job, done) => {

  // Call the sendNotification function with the job data
  sendNotification(job.data.phoneNumber, job.data.message);

  // Mark the job as completed
  done();
});
