import struct 
from zlib import crc32 

from .connection import Connection ,PacketCodec 
from ...errors import InvalidChecksumError ,InvalidBufferError 

class FullPacketCodec (PacketCodec ):
    tag =None 

    def __init__ (self ,connection ):
        super ().__init__ (connection )
        self ._send_counter =0 

    def encode_packet (self ,data ):

        length =len (data )+12 
        data =struct .pack ('<ii',length ,self ._send_counter )+data 
        crc =struct .pack ('<I',crc32 (data ))
        self ._send_counter +=1 
        return data +crc 

    async def read_packet (self ,reader ):
        packet_len_seq =await reader .readexactly (8 )
        packet_len ,seq =struct .unpack ('<ii',packet_len_seq )
        if packet_len <0 and seq <0 :

            body =await reader .readexactly (4 )
            raise InvalidBufferError (body )

        body =await reader .readexactly (packet_len -8 )
        checksum =struct .unpack ('<I',body [-4 :])[0 ]
        body =body [:-4 ]

        valid_checksum =crc32 (packet_len_seq +body )
        if checksum !=valid_checksum :
            raise InvalidChecksumError (checksum ,valid_checksum )

        return body 

class ConnectionTcpFull (Connection ):
    """"""
    packet_codec =FullPacketCodec 
