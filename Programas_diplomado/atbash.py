#Función para usar cifrado Atbash
def atbash(message):
    alphabet = u'A B C D E F G H I J K L M N Ñ O P Q R S T U V W X Y Z'.split()
    backward = u'Z Y X W V U T S R Q P O Ñ N M L K J I H G F E D C B A'.split()
    cipher = []
    
    for letter in message:
        if letter in alphabet:
            for i in range(len(alphabet)):
                if alphabet[i] == letter:
                    pos = i
            cipher.append(backward[pos])
        else:
            cipher.append(letter)
    
    newMessage = ''.join(cipher)
    return newMessage

crypt = atbash(u'ZKIVNWV XLÑL HR UFVIZ Z ERERI GLWZ OZ ERWZ B EREV XLÑL HR UFVIZH Z ÑLIRI ÑZMZNZ')
print (crypt)