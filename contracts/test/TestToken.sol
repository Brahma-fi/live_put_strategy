// SPDX-License-Identifier: MIT
pragma solidity >=0.7.5;

import '@openzeppelin/contracts/token/ERC20/ERC20.sol';

contract TestToken is ERC20 {
    constructor(
        string memory name_,
        string memory symbol_,
        uint256 amount,
        address mintTo
    ) ERC20(name_, symbol_) {
        _mint(mintTo, amount);
    }
}
