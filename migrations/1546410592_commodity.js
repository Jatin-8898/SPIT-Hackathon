var Commodity = artifacts.require("./Commodity.sol");

module.exports = function(deployer) {
  // Use deployer to state migration tasks.
  deployer.deploy(Commodity);
};
