import rsa
import pickle
 
 
def RsaEncrypt(str):
    (PubKey, PrivateKey) = rsa.newkeys(512)
    content = str.encode('utf8')
    Encrypt_Str = rsa.encrypt(content, PubKey)
    return (Encrypt_Str, PrivateKey)
 
 
def RsaDecrypt(str, pk):
    Decrypt_Str = rsa.decrypt(str, pk)
    Decrypt_Str_1 = Decrypt_Str.decode('utf8')
    return Decrypt_Str_1
 
 
def SendMessage(SendData):
    (encryptdata, PrivateKey) = RsaEncrypt(SendData)
    # print('encrypted data is ' + str(encryptdata))
    Message = pickle.dumps([encryptdata, PrivateKey])
    return Message
 
 
def RecvMessage(Message):
    (recvdata, PrivateKey) = pickle.loads(Message)
    decryptdata = RsaDecrypt(recvdata, PrivateKey)
    # print('decrypted data is ' + str(decryptdata))
    return decryptdata


if __name__ == '__main__':
    Message = SendMessage("1")
    RecvMessage(Message)
 
 
