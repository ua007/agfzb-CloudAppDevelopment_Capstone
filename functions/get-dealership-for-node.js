// IBM Action, method=GET, node.js v12
// xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

const Cloudant = require('@cloudant/cloudant'); 

function main(params) {

    secret={
    "COUCH_URL": "https://20c446e9-b7d6-47c4-9aba-260d13815831-bluemix.cloudantnosqldb.appdomain.cloud",
    "IAM_API_KEY": "ng9v3anfOCobH63DPcohiQERqqu4Bdcm-oXVH40ntjU5",
    "COUCH_USERNAME": "20c446e9-b7d6-47c4-9aba-260d13815831-bluemix"}

    return new Promise(function (resolve, reject) {
    const cloudant = Cloudant({
        url: secret.COUCH_URL,
        plugins: { iamauth: { iamApiKey: secret.IAM_API_KEY } }
    });
    const dealershipDb = cloudant.use('dealerships');

    if (params.state) {
        // return dealership with this state 
        dealershipDb.find({
            "selector": {
                "state": {
                    "$eq": params.state
                }
            }
        }, function (err, result) {
            if (err) {
                reject(err);
            }
            let code = 200;
            if (result.docs.length == 0) {
                code = 404;
            }
            resolve({
                statusCode: code,
                headers: { 'Content-Type': 'application/json' },
                body: result
            });
        });
    } else if (params.id) {
        id = parseInt(params.dealerId)
        // return dealership with this state 
        dealershipDb.find({ selector: { id: parseInt(params.id) } }, function (err, result) {
            if (err) {
                reject(err);
            }
            let code = 200;
            if (result.docs.length == 0) {
                code = 404;
            }
            resolve(
                {
                    statusCode: code,
                    headers: { 'Content-Type': 'application/json' },
                    body: result
                });
        });
    } else {     // return all documents 
        dealershipDb.list({ include_docs: true }, function (err, result) {
            if (err) {
                reject(err);
            }
            resolve({
                statusCode: 200,
                headers: { 'Content-Type': 'application/json' },
                body: result
            });
        });
    }
});
   
};
