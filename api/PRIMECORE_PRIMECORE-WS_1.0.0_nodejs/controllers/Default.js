'use strict';

var url = require('url');

var Default = require('./DefaultService');

module.exports.accessPointCountGET = function accessPointCountGET (req, res, next) {
  Default.accessPointCountGET(req.swagger.params, res, next);
};

module.exports.accessPointGET = function accessPointGET (req, res, next) {
  Default.accessPointGET(req.swagger.params, res, next);
};

module.exports.accessPointIdGET = function accessPointIdGET (req, res, next) {
  Default.accessPointIdGET(req.swagger.params, res, next);
};

module.exports.accessPointNameDeviceTypeCountGET = function accessPointNameDeviceTypeCountGET (req, res, next) {
  Default.accessPointNameDeviceTypeCountGET(req.swagger.params, res, next);
};

module.exports.accessPointNameTotalUsernamesGET = function accessPointNameTotalUsernamesGET (req, res, next) {
  Default.accessPointNameTotalUsernamesGET(req.swagger.params, res, next);
};

module.exports.buildingGET = function buildingGET (req, res, next) {
  Default.buildingGET(req.swagger.params, res, next);
};

module.exports.networkMetricBuildingGET = function networkMetricBuildingGET (req, res, next) {
  Default.networkMetricBuildingGET(req.swagger.params, res, next);
};

module.exports.rogueAccessPointAlarmCountGET = function rogueAccessPointAlarmCountGET (req, res, next) {
  Default.rogueAccessPointAlarmCountGET(req.swagger.params, res, next);
};

module.exports.rogueAccessPointAlarmGET = function rogueAccessPointAlarmGET (req, res, next) {
  Default.rogueAccessPointAlarmGET(req.swagger.params, res, next);
};

module.exports.rogueAccessPointAlarmIdGET = function rogueAccessPointAlarmIdGET (req, res, next) {
  Default.rogueAccessPointAlarmIdGET(req.swagger.params, res, next);
};
