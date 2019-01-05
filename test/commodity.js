var Commodity = artifacts.require("Commodity");

contract('commodity', function(accounts) {
  var admin = accounts[0];
  var distributors = [accounts[1],accounts[2],accounts[3]];

  it("admin should be first account",function(){
      return Commodity.deployed().then(function(instance){
      instance.getAdmin().then(function(result){
        assert.equal(result,admin);
      });
    });
  });

  it("allocates right amount of foodgrains to distributor",function(){
    var distributor = distributors[0];
    return Commodity.deployed().then(function(instance){
      instance.allocate(distributor,100,75,50,{from:admin}).then(function(){
        return app.distributors(distributor);
      }).then(function(result){
        assert.equal(result[0],211);
      });
    });
  });
});
