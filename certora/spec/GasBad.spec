/*
* Verification of Gas Bad Nft Marketplace
*/ 

// Methods

methods {
    function _.safeTransferFrom(address, address, uint256) external => DISPATCHER(true);
    function _.onERC721Received(address,address,uint256,bytes) external => DISPATCHER(true);
}

// Ghost variables

ghost mathint listingUpdatesCount
{
    init_state axiom listingUpdatesCount == 0;
}
ghost mathint log4Count
{
    init_state axiom log4Count == 0;
}

// Hooks

hook Sstore s_listings[KEY address nftAddress][KEY uint256 tokenId].price uint256 price{
    listingUpdatesCount = listingUpdatesCount +1;
}

hook LOG4(uint offset, uint length, bytes32 t1, bytes32 t2, bytes32 t3, bytes32 t4){
    log4Count = log4Count +1;
}

// Rules

invariant mapping_update_emits_event()
    listingUpdatesCount <= log4Count;