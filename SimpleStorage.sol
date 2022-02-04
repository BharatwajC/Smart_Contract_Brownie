//SPDX - license-identifier.MIT
pragma solidity ^0.6.0;

contract SimpleStorage {
    uint256 private favouriteNum;

    struct People {
        uint256 fnum;
        string name;
    }

    People[] public people;

    People public person = People({fnum: 11, name: "Neymar"});

    mapping(string => uint256) public nameToFavouriteNumber;

    function addPerson(string memory _name, uint256 _favnum) public {
        people.push(People({fnum: _favnum, name: _name}));
        nameToFavouriteNumber[_name] = _favnum;
    }

    //

    function store(uint256 _favNum) public {
        favouriteNum = _favNum;
    }

    function retrieve() public view returns (uint256) {
        return favouriteNum;
    }
}

// brownie compile
