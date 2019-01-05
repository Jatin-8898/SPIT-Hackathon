pragma solidity ^0.5.0;

contract Commodity {
  address admin;

  event BufferStatusChanged(
    address distributorId,
    uint rice,
    uint wheat,
    uint coarse
  );

  event Sold(
    address beneficiaryId,
    uint rice,
    uint wheat,
    uint coarse
  );

  struct FoodGrains{
    uint rice;
    uint wheat;
    uint coarse;
  }

  struct BeneficiaryData{
    address beneficiary;
    address distributor;
	bytes1 date;
    uint rice;
    uint wheat;
    uint coarse;
  }
  
  mapping(address => FoodGrains) public distributors;

  mapping(uint => address) addressIndices;
  mapping(address => mapping(bytes3 => BeneficiaryData)) public beneficiaryData;
  uint addressCount;

  constructor() public {
	addressCount = 0;
    admin = msg.sender;
  }

  function getAdmin() public view returns (address x){
    return admin;
  }

  function allocate(address distributorId,uint rice,uint wheat,uint coarse) public {
    require(msg.sender == admin);

    FoodGrains memory grains = distributors[distributorId];

    uint newRice = grains.rice + rice;
    uint newWheat = grains.wheat + wheat;
    uint newCoarse = grains.coarse + coarse;    

    distributors[distributorId] = FoodGrains(newRice,newWheat,newCoarse);
    emit BufferStatusChanged(distributorId,rice,wheat,coarse);
  }

  function sell(address beneficiaryId,bytes1 date,bytes3 monthYear,uint rice,uint wheat,uint coarse) public {
    FoodGrains memory grains = distributors[msg.sender];

    uint newRice = grains.rice - rice;
    uint newWheat = grains.wheat - wheat;
    uint newCoarse = grains.coarse - coarse;

    distributors[msg.sender] = FoodGrains(newRice,newWheat,newCoarse);

	
    beneficiaryData[beneficiaryId][monthYear] = BeneficiaryData(beneficiaryId,msg.sender,date,rice,wheat,coarse);
	
	emit BufferStatusChanged(msg.sender,newRice,newWheat,newCoarse);
    emit Sold(beneficiaryId,rice,wheat,coarse);
  }

}
