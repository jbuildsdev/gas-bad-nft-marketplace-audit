// rule sanity {
//     satisfy true;
// }

// invariant totalSupplyInNotNegative()
//     totalSupply() >=0;

using NftMock as nft;

methods {
    function totalSupply() external returns uint256 envfree;
    function mint() external;
    function balanceOf(address) external returns uint256 envfree;
}



rule minting_mints_one_nft() {
    //Arrange
    env e;
    address minter;
    require e.msg.value == 0;
    require e.msg.sender == minter;

    mathint balanceBefore = nft.balanceOf(minter);

    //Act
    currentContract.mint(e);

    //Assert
    assert to_mathint(nft.balanceOf(minter)) == balanceBefore+1, "Only 1 NFT should be minted per mint call";
}