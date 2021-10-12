'use strict';

exports.accessPointCountGET = function(args, res, next) {
  /**
   *
   * returns inline_response_200_1
   **/
  var examples = {};
  examples['application/json'] = {
  "count" : 0.80082819046101150206595775671303272247314453125
};
  if (Object.keys(examples).length > 0) {
    res.setHeader('Content-Type', 'application/json');
    res.end(JSON.stringify(examples[Object.keys(examples)[0]] || {}, null, 2));
  } else {
    res.end();
  }
}

exports.accessPointGET = function(args, res, next) {
  /**
   *
   * maxResult BigDecimal max number of results returned (limited to 1000 by the backend) (optional)
   * firstResult BigDecimal first result index to be returned (optional)
   * returns inline_response_200
   **/
  var examples = {};
  examples['application/json'] = {
  "last" : 6.02745618307040320615897144307382404804229736328125,
  "count" : 1.46581298050294517310021547018550336360931396484375,
  "accessPoints" : [ {
    "upTime" : 9.301444243932575517419536481611430644989013671875,
    "macAddress" : "aeiou",
    "clientCount_5GHz" : 7.061401241503109105224211816675961017608642578125,
    "name" : "aeiou",
    "location" : "aeiou",
    "model" : "aeiou",
    "id" : 5.962133916683182377482808078639209270477294921875,
    "type" : "aeiou",
    "clientCount" : 5.63737665663332876420099637471139430999755859375,
    "clientCount_2_4GHz" : 2.3021358869347654518833223846741020679473876953125,
    "status" : "CRITICAL"
  } ],
  "first" : 0.80082819046101150206595775671303272247314453125
};
  if (Object.keys(examples).length > 0) {
    res.setHeader('Content-Type', 'application/json');
    res.end(JSON.stringify(examples[Object.keys(examples)[0]] || {}, null, 2));
  } else {
    res.end();
  }
}

exports.accessPointIdGET = function(args, res, next) {
  /**
   *
   * id String id
   * returns AccessPointObject
   **/
  var examples = {};
  examples['application/json'] = {
  "upTime" : 5.63737665663332876420099637471139430999755859375,
  "macAddress" : "aeiou",
  "clientCount_5GHz" : 5.962133916683182377482808078639209270477294921875,
  "name" : "aeiou",
  "location" : "aeiou",
  "model" : "aeiou",
  "id" : 0.80082819046101150206595775671303272247314453125,
  "type" : "aeiou",
  "clientCount" : 6.02745618307040320615897144307382404804229736328125,
  "clientCount_2_4GHz" : 1.46581298050294517310021547018550336360931396484375,
  "status" : "CRITICAL"
};
  if (Object.keys(examples).length > 0) {
    res.setHeader('Content-Type', 'application/json');
    res.end(JSON.stringify(examples[Object.keys(examples)[0]] || {}, null, 2));
  } else {
    res.end();
  }
}

exports.accessPointNameDeviceTypeCountGET = function(args, res, next) {
  /**
   *
   * name String name
   * returns inline_response_200_2
   **/
  var examples = {};
  examples['application/json'] = {
  "deviceTypeCounts" : [ {
    "deviceType" : "aeiou",
    "count" : 0.80082819046101150206595775671303272247314453125
  } ]
};
  if (Object.keys(examples).length > 0) {
    res.setHeader('Content-Type', 'application/json');
    res.end(JSON.stringify(examples[Object.keys(examples)[0]] || {}, null, 2));
  } else {
    res.end();
  }
}

exports.accessPointNameTotalUsernamesGET = function(args, res, next) {
  /**
   *
   * name String name
   * returns inline_response_200_1
   **/
  var examples = {};
  examples['application/json'] = {
  "count" : 0.80082819046101150206595775671303272247314453125
};
  if (Object.keys(examples).length > 0) {
    res.setHeader('Content-Type', 'application/json');
    res.end(JSON.stringify(examples[Object.keys(examples)[0]] || {}, null, 2));
  } else {
    res.end();
  }
}

exports.buildingGET = function(args, res, next) {
  /**
   *
   * returns inline_response_200_4
   **/
  var examples = {};
  examples['application/json'] = {
  "buildings" : [ "aeiou" ]
};
  if (Object.keys(examples).length > 0) {
    res.setHeader('Content-Type', 'application/json');
    res.end(JSON.stringify(examples[Object.keys(examples)[0]] || {}, null, 2));
  } else {
    res.end();
  }
}

exports.networkMetricBuildingGET = function(args, res, next) {
  /**
   *
   * building String building
   * metric String metric to fetch (tx or rx)
   * timeInterval BigDecimal time interval, integer (hours) (optional)
   * returns MetricsObject
   **/
  var examples = {};
  examples['application/json'] = {
  "metricsData" : {
    "metricName" : "aeiou",
    "values" : [ {
      "XValue" : 6.02745618307040320615897144307382404804229736328125,
      "YValues" : [ 1.46581298050294517310021547018550336360931396484375 ]
    } ],
    "currentDateTime" : 0.80082819046101150206595775671303272247314453125,
    "description" : "aeiou",
    "XValueProperty" : {
      "unit" : "aeiou",
      "label" : "aeiou"
    },
    "YValueProperty" : {
      "unit" : "aeiou",
      "maxVal" : 5.962133916683182377482808078639209270477294921875,
      "minVal" : 5.63737665663332876420099637471139430999755859375
    }
  }
};
  if (Object.keys(examples).length > 0) {
    res.setHeader('Content-Type', 'application/json');
    res.end(JSON.stringify(examples[Object.keys(examples)[0]] || {}, null, 2));
  } else {
    res.end();
  }
}

exports.rogueAccessPointAlarmCountGET = function(args, res, next) {
  /**
   *
   * returns inline_response_200_1
   **/
  var examples = {};
  examples['application/json'] = {
  "count" : 0.80082819046101150206595775671303272247314453125
};
  if (Object.keys(examples).length > 0) {
    res.setHeader('Content-Type', 'application/json');
    res.end(JSON.stringify(examples[Object.keys(examples)[0]] || {}, null, 2));
  } else {
    res.end();
  }
}

exports.rogueAccessPointAlarmGET = function(args, res, next) {
  /**
   *
   * maxResult BigDecimal max number of results returned (limited to 1000 by the backend) (optional)
   * firstResult BigDecimal first result index to be returned (optional)
   * returns inline_response_200_3
   **/
  var examples = {};
  examples['application/json'] = {
  "last" : 6.02745618307040320615897144307382404804229736328125,
  "count" : 1.46581298050294517310021547018550336360931396484375,
  "accessPoints" : [ {
    "severity" : "CRITICAL",
    "timeStamp" : "aeiou",
    "lastUpdatedAt" : "aeiou",
    "rogueApAlarmDetails" : {
      "rssi" : 2.3021358869347654518833223846741020679473876953125,
      "macAddress" : "aeiou",
      "classificationType" : "FRIENDLY",
      "location" : "aeiou",
      "state" : "INITIALIZING",
      "rogueClients" : 5.63737665663332876420099637471139430999755859375,
      "ssid" : "aeiou"
    },
    "acknowledgementStatus" : true,
    "wirelessSpecificAlarmId" : "aeiou",
    "id" : 5.962133916683182377482808078639209270477294921875,
    "message" : "aeiou",
    "deviceName" : "aeiou",
    "alarmFoundAt" : "aeiou"
  } ],
  "first" : 0.80082819046101150206595775671303272247314453125
};
  if (Object.keys(examples).length > 0) {
    res.setHeader('Content-Type', 'application/json');
    res.end(JSON.stringify(examples[Object.keys(examples)[0]] || {}, null, 2));
  } else {
    res.end();
  }
}

exports.rogueAccessPointAlarmIdGET = function(args, res, next) {
  /**
   *
   * id String id
   * returns RogueAccessPointAlarmObject
   **/
  var examples = {};
  examples['application/json'] = {
  "severity" : "CRITICAL",
  "timeStamp" : "aeiou",
  "lastUpdatedAt" : "aeiou",
  "rogueApAlarmDetails" : {
    "rssi" : 1.46581298050294517310021547018550336360931396484375,
    "macAddress" : "aeiou",
    "classificationType" : "FRIENDLY",
    "location" : "aeiou",
    "state" : "INITIALIZING",
    "rogueClients" : 6.02745618307040320615897144307382404804229736328125,
    "ssid" : "aeiou"
  },
  "acknowledgementStatus" : true,
  "wirelessSpecificAlarmId" : "aeiou",
  "id" : 0.80082819046101150206595775671303272247314453125,
  "message" : "aeiou",
  "deviceName" : "aeiou",
  "alarmFoundAt" : "aeiou"
};
  if (Object.keys(examples).length > 0) {
    res.setHeader('Content-Type', 'application/json');
    res.end(JSON.stringify(examples[Object.keys(examples)[0]] || {}, null, 2));
  } else {
    res.end();
  }
}

