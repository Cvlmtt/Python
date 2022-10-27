""""Scrivere una classe MyProxy che è il proxy della classe MyClass.
 Ogni volta che viene invocato un metodo di istanza della classe MyProxy
 di fatto viene invocato l'omonimo metodo di MyCLass. Non deve essere
 usata l'ereditarietà.

 Si assuma che __init__ di MyClass prenda in input un argomento x e che i
 comportamente dei suoi metodi di istanza dipenda dal valore di x passati a __init__
 """

from MyProxy import MyProxy

x = MyProxy(10)

x.f()

x.g()