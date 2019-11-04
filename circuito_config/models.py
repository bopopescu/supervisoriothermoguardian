from django.db import models
import serial

# Create your models here.

class Circuito(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nome

class Modulo(models.Model):
    #paridade:
    NONE = serial.PARITY_NONE
    EVEN = serial.PARITY_EVEN
    ODD = serial.PARITY_ODD
    MARK = serial.PARITY_MARK
    SPACE = serial.PARITY_SPACE

    PARIDADE = [
        (NONE, 'None'),
        (EVEN, 'Even'),
        (ODD, 'Odd'),
        (MARK, 'Mark'),
        (SPACE, 'Space'),
    ]

    circuito = models.ForeignKey(Circuito, on_delete=models.CASCADE)
    fabricante = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    patrimonio = models.CharField(max_length=100, null=True, blank=True)
    no_slave = models.IntegerField()
    porta = models.CharField(max_length=255)
    baudrate = models.IntegerField()
    parity = models.CharField(max_length=1, choices=PARIDADE, default=NONE)
    bytesize = models.IntegerField()
    stopbits = models.IntegerField()
    timeout = models.IntegerField()

    def __str__(self):
        return str(self.no_slave)


class Parametro(models.Model):

    #data Type
    bits8 = '8'
    bits16 = '16'
    bits32 = '32'

    DATATYPE = [
        (bits8, '8 bits'),
        (bits16, '16 bits'),
        (bits32, '32 bits'),
    ]

    #unidades
    BAR = 'bar'
    CELSIUS = 'celsius'
    SEGUNDOS = 'segundos'
    PERCENTUAL = 'percentual'
    SEM_UNIDADE = 'sem'

    UNIDADE = [
        (BAR, 'bar(g)'),
        (CELSIUS, '˚C'),
        (SEGUNDOS, 'segundos'),
        (PERCENTUAL, '%'),
        (SEM_UNIDADE, 'sem unidade definida'),
    ]

    modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255, blank=True, null=True)
    endereco = models.IntegerField()
    escala = models.IntegerField()
    ativo = models.BooleanField(default=True)
    datatype = models.CharField(max_length=2, choices=DATATYPE, default=bits16)
    unidade = models.CharField(max_length=20, choices=UNIDADE, default=SEM_UNIDADE)


    def __str__(self):
        return str(self.endereco)

class Datalog(models.Model):
    valor = models.FloatField()
    datahora = models.DateTimeField(auto_now_add=True)
    parametro = models.ForeignKey(Parametro, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.valor)

