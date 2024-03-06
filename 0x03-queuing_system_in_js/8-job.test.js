const createPushNotificationsJobs = require('./8-job');
import kue from 'kue';
import chai from 'chai';
const queue = kue.createQueue();
const expect = chai.expect;

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  },
];

describe('createPushNotificationsJobs', () => {
  before(() => {
    queue.testMode.enter();
  });

  afterEach(async () => {
    await queue.testMode.clear();
  });

  after(() => {
    queue.testMode.exit();
  });

  it('throws an error if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs('not_an_array', queue)).to.throw('Jobs is not an array');
  });
  it('creates jobs in the queue with correct logging', () => {
    createPushNotificationsJobs(jobs, queue);
    expect(queue.testMode.jobs.length).to.equal(2);

    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');

    expect(queue.testMode.jobs[0].data).to.eql(jobs[0]);

    expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
  });
});
