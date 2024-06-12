//SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@chainlink/contracts/src/v0.8/shared/interfaces/AggregatorV3Interface.sol";

contract fundme {
    mapping(address => uint256) public addresstoval;
    uint256 public msgstore;
    address public owner;
    address[] public funded;
    AggregatorV3Interface public pricefeedcontract;

    constructor(address pricefeed) {
        pricefeedcontract = AggregatorV3Interface(pricefeed);
        owner = msg.sender;
    }
    modifier OnlyOwner() {
        require(msg.sender == owner);
        _;
    }

    function fund() public payable {
        uint256 minimum = 50 * 10 ** 18;
        require(
            getconversionrate(msg.value) >= minimum,
            "Minimum fund must be greater than $50"
        );
        addresstoval[msg.sender] += msg.value;
        msgstore += getconversionrate(msg.value);
        funded.push(msg.sender);
    }

    function getentrancefee() public view returns (uint256) {
        uint256 minimumUSD = 50 * 10 ** 18;
        uint256 price = getprice();
        uint256 precision = 1 * 10 ** 18;
        return (minimumUSD * precision) / price;
    }
    function getprice() public view returns (uint256) {
        (, int256 answer, , , ) = pricefeedcontract.latestRoundData();
        return uint256(answer * 10000000000);
    }
    function getconversionrate(
        uint256 ethamount
    ) public view returns (uint256) {
        uint256 ethprice = getprice();
        uint256 ethtousd = (ethamount * ethprice) / 1000000000000000000;
        return ethtousd;
    }

    function withdraw() public payable OnlyOwner {
        payable(msg.sender).transfer(address(this).balance);
        for (uint256 funderindex; funderindex < funded.length; funderindex++) {
            addresstoval[funded[funderindex]] = 0;
        }
        funded = new address[](0);
    }
}
