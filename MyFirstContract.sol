pragma solidity ^0.6.8;

contract MyFirstContract {
    
    string fName;
    uint age;
    
    function setInstructor(string _fName, uint _age) public  {
        fName = _fName;
        age   = _age;
    }
    
    function getInstructor() view public returns(string, uint) {
    return(fName, age);
    }
    
    
}

수정된 버전.

// SPDX-License-Identifier: MIT

pragma solidity ^0.6.8;
contract MyFirstContract2 {
    string fName;
   	uint age;
   	event Instructor(
   		string name,
   		uint age
	);
    function setInstructor(string memory _fName, uint _age) public {
        fName = _fName;
        age = _age;
        emit Instructor(_fName, _age);        // Add this
    }
    function getInstructor() view public returns (string memory, uint) {
        return (fName, age);
    }
}
