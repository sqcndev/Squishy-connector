linux_d = './komodod -ac_name=SQCN '
windows_d = 'komodod.exe -ac_name=SQCN '
linux_cli = './komodo-cli -ac_name=SQCN '
windows_cli = 'komodo-cli.exe -ac_name=SQCN '
squishyd = '-ac_supply=1468750 -ac_eras=6 -ac_blocktime=420 -ac_reward=10000000000,2500000000,1250000000,625000000,312500000,156250000 -ac_end=10000,100000,500000,1500000,2500000,5000000 -ac_staked=25 -ac_sapling=1 -ac_cbmaturity=6 -ac_cc=0 -addressindex=1 -spentindex=1 -addnode=146.190.69.236 -addnode=64.225.91.174'
getinfo = "getinfo"
validateaddress = 'validateaddress'
getaddressesbyaccount = 'getaddressesbyaccount'
listaddressgroupings = 'listaddressgroupings'
setpubkey = 'setpubkey'
getnewaddress = 'getnewaddress'
stop = 'stop'
squishyunlock = 'squishyunlock'
squishylock = 'squishylock'
getbalance = 'getbalance'
getgenerate = 'getgenerate'
setgenerate = 'setgenerate'  # + True "number" or False
getaddressbalance = 'getaddressbalance'  # +  '{"addresses": ["address"]}'
convertpassphrase = 'convertpassphrase'  # + "agamapassphrase"
importprivkey = 'importprivkey'  # + "wifkey"
dumpprivkey = 'dumpprivkey'  # + "address"
squishyinfo = 'squishyinfo'  # firstheight + lastheight + minamount + maxamount + pubkey
sendrawtransaction = 'sendrawtransaction'  # + hex
squishyreceivelist = 'squishyreceivelist'  # + pubkey + maxage
sendtoaddress = 'sendtoaddress'  # + amount
squishycreditloop = 'squishycreditloop'  # + txid
squishyreceive = 'squishyreceive'  # case 1: + senderpk + amount + currency + matures + '{"avalcount":"n"}' case 2:
# senderpk batontxid '{"avalcount":"n"}'
squishytransfer = 'squishytransfer'  # + receiverpk + '{"avalcount":"n"}' + requesttxid
squishyissue = 'squishyissue'  # receiverpk + '{"avalcount":"n", "autosettlement":"true"|"false",
# "autoinsurance":"true"|"false", "disputeexpires":"offset", "EscrowOn":"true"|"false", "BlockageAmount":"amount" }'
# + requesttxid
squishyholderloops = 'squishyholderloops'  # firstheight + lastheight + minamount + maxamount + pk + [currency]
getaddresstxids = 'getaddresstxids'  # '{"addresses": ["address"], "start": 799712,  "end": 799734}'
squishylistactivatedaddresses = 'squishylistactivatedaddresses'
gettransaction = 'gettransaction'  # + txid
getblock = 'getblock'  # + block
getrawtransaction = 'getrawtransaction'  # + txid
decoderawtransaction = 'decoderawtransaction'  # rawtxid
