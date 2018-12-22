// Download the helper library from https://www.twilio.com/docs/node/install
// Your Account Sid and Auth Token from twilio.com/console
const accountSid = 'AC9c2a97b7b1f8c217c936c8a4da93c6d6';
const authToken = 'your_auth_token';
const client = require('twilio')(accountSid, authToken);

client.messages
      .create({from: '+15017122661', body: 'body', to: '+919994878015'})
      .then(message => console.log(message.sid))
      .done();