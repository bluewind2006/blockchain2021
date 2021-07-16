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
