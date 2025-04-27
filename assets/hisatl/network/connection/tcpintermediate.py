import struct 
import random 
import os 

from .connection import Connection ,PacketCodec 

class IntermediatePacketCodec (PacketCodec ):
    tag =b'\xee\xee\xee\xee'
    obfuscate_tag =tag 

    def encode_packet (self ,data ):
        return struct .pack ('<i',len (data ))+data 

    async def read_packet (self ,reader ):
        length =struct .unpack ('<i',await reader .readexactly (4 ))[0 ]
        return await reader .readexactly (length )

class RandomizedIntermediatePacketCodec (IntermediatePacketCodec ):
    """"""
    tag =None 
    obfuscate_tag =b'\xdd\xdd\xdd\xdd'

    def encode_packet (self ,data ):
        pad_size =random .randint (0 ,3 )
        padding =os .urandom (pad_size )
        return super ().encode_packet (data +padding )

    async def read_packet (self ,reader ):
        packet_with_padding =await super ().read_packet (reader )
        pad_size =len (packet_with_padding )%4 
        if pad_size >0 :
            return packet_with_padding [:-pad_size ]
        return packet_with_padding 

class ConnectionTcpIntermediate (Connection ):
    """"""
    packet_codec =IntermediatePacketCodec 
