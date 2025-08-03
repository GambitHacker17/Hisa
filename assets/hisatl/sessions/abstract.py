from abc import ABC ,abstractmethod 

class Session (ABC ):
    def __init__ (self ):
        pass 

    def clone (self ,to_instance =None ):
        """"""
        return to_instance or self .__class__ ()

    @abstractmethod 
    def set_dc (self ,dc_id ,server_address ,port ):
        """"""
        raise NotImplementedError 

    @property 
    @abstractmethod 
    def dc_id (self ):
        """"""
        raise NotImplementedError 

    @property 
    @abstractmethod 
    def server_address (self ):
        """"""
        raise NotImplementedError 

    @property 
    @abstractmethod 
    def port (self ):
        """"""
        raise NotImplementedError 

    @property 
    @abstractmethod 
    def auth_key (self ):
        """"""
        raise NotImplementedError 

    @auth_key .setter 
    @abstractmethod 
    def auth_key (self ,value ):
        """"""
        raise NotImplementedError 

    @property 
    @abstractmethod 
    def takeout_id (self ):
        """"""
        raise NotImplementedError 

    @takeout_id .setter 
    @abstractmethod 
    def takeout_id (self ,value ):
        """"""
        raise NotImplementedError 

    @abstractmethod 
    def get_update_state (self ,entity_id ):
        """"""
        raise NotImplementedError 

    @abstractmethod 
    def set_update_state (self ,entity_id ,state ):
        """"""
        raise NotImplementedError 

    @abstractmethod 
    def get_update_states (self ):
        """"""

    def close (self ):
        """"""

    @abstractmethod 
    def save (self ):
        """"""
        raise NotImplementedError 

    @abstractmethod 
    def delete (self ):
        """"""
        raise NotImplementedError 

    @classmethod 
    def list_sessions (cls ):
        """"""
        return []

    @abstractmethod 
    def process_entities (self ,tlo ):
        """"""
        raise NotImplementedError 

    @abstractmethod 
    def get_input_entity (self ,key ):
        """"""
        raise NotImplementedError 

    @abstractmethod 
    def cache_file (self ,md5_digest ,file_size ,instance ):
        """"""
        raise NotImplementedError 

    @abstractmethod 
    def get_file (self ,md5_digest ,file_size ,cls ):
        """"""
        raise NotImplementedError 
