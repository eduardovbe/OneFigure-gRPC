# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from proto import message_pb2 as proto_dot_message__pb2


class MessageStub(object):
    """Comando para gerar o proto:
    python -m grpc_tools.protoc --proto_path=. .\proto\message.proto --python_out=. --grpc_python_out=.

    Como escrever em PROTO
    https://developers.google.com/protocol-buffers/docs/proto3

    Como enviar um array de dados
    https://stackoverflow.com/questions/43167762/how-to-return-an-array-in-protobuf-service-rpc
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Login = channel.unary_unary(
                '/proto.Message/Login',
                request_serializer=proto_dot_message__pb2.MessageClient.SerializeToString,
                response_deserializer=proto_dot_message__pb2.LoginResponse.FromString,
                )
        self.Create = channel.unary_unary(
                '/proto.Message/Create',
                request_serializer=proto_dot_message__pb2.MessageClient.SerializeToString,
                response_deserializer=proto_dot_message__pb2.Response.FromString,
                )
        self.Album = channel.unary_unary(
                '/proto.Message/Album',
                request_serializer=proto_dot_message__pb2.MessageClient.SerializeToString,
                response_deserializer=proto_dot_message__pb2.AlbumResponse.FromString,
                )
        self.Buy = channel.unary_unary(
                '/proto.Message/Buy',
                request_serializer=proto_dot_message__pb2.MessageClient.SerializeToString,
                response_deserializer=proto_dot_message__pb2.AlbumResponse.FromString,
                )
        self.Sell = channel.unary_unary(
                '/proto.Message/Sell',
                request_serializer=proto_dot_message__pb2.MessageClient.SerializeToString,
                response_deserializer=proto_dot_message__pb2.SellResponse.FromString,
                )


class MessageServicer(object):
    """Comando para gerar o proto:
    python -m grpc_tools.protoc --proto_path=. .\proto\message.proto --python_out=. --grpc_python_out=.

    Como escrever em PROTO
    https://developers.google.com/protocol-buffers/docs/proto3

    Como enviar um array de dados
    https://stackoverflow.com/questions/43167762/how-to-return-an-array-in-protobuf-service-rpc
    """

    def Login(self, request, context):
        """Chamar a função Login do servidor passando a mensagem LOGIN do cliente
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Chama a função do servidor para cadastrar um novo usuário
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Album(self, request, context):
        """Chama a função do servidor para visualizar o álbum
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Buy(self, request, context):
        """Chama a função do servidor que realiza a compra e exibe as figurinhas
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Sell(self, request, context):
        """Chama a função venda e mostra as figuras adquiridas
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MessageServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Login': grpc.unary_unary_rpc_method_handler(
                    servicer.Login,
                    request_deserializer=proto_dot_message__pb2.MessageClient.FromString,
                    response_serializer=proto_dot_message__pb2.LoginResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=proto_dot_message__pb2.MessageClient.FromString,
                    response_serializer=proto_dot_message__pb2.Response.SerializeToString,
            ),
            'Album': grpc.unary_unary_rpc_method_handler(
                    servicer.Album,
                    request_deserializer=proto_dot_message__pb2.MessageClient.FromString,
                    response_serializer=proto_dot_message__pb2.AlbumResponse.SerializeToString,
            ),
            'Buy': grpc.unary_unary_rpc_method_handler(
                    servicer.Buy,
                    request_deserializer=proto_dot_message__pb2.MessageClient.FromString,
                    response_serializer=proto_dot_message__pb2.AlbumResponse.SerializeToString,
            ),
            'Sell': grpc.unary_unary_rpc_method_handler(
                    servicer.Sell,
                    request_deserializer=proto_dot_message__pb2.MessageClient.FromString,
                    response_serializer=proto_dot_message__pb2.SellResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'proto.Message', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Message(object):
    """Comando para gerar o proto:
    python -m grpc_tools.protoc --proto_path=. .\proto\message.proto --python_out=. --grpc_python_out=.

    Como escrever em PROTO
    https://developers.google.com/protocol-buffers/docs/proto3

    Como enviar um array de dados
    https://stackoverflow.com/questions/43167762/how-to-return-an-array-in-protobuf-service-rpc
    """

    @staticmethod
    def Login(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.Message/Login',
            proto_dot_message__pb2.MessageClient.SerializeToString,
            proto_dot_message__pb2.LoginResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.Message/Create',
            proto_dot_message__pb2.MessageClient.SerializeToString,
            proto_dot_message__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Album(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.Message/Album',
            proto_dot_message__pb2.MessageClient.SerializeToString,
            proto_dot_message__pb2.AlbumResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Buy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.Message/Buy',
            proto_dot_message__pb2.MessageClient.SerializeToString,
            proto_dot_message__pb2.AlbumResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Sell(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.Message/Sell',
            proto_dot_message__pb2.MessageClient.SerializeToString,
            proto_dot_message__pb2.SellResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)