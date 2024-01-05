import json
from models.modelo import Modelo

class Jogador:
  def __init__(self, id, nome, email, idTime, senha, idade, nCamisa):
    self.__id = id
    self.__nome = nome
    self.__email = email
    self.__idTime = idTime
    self.__senha = senha
    self.__idade = idade
    self.__nCamisa = nCamisa

  def get_id(self): return self.__id
  def get_nome(self): return self.__nome
  def get_email(self): return self.__email
  def get_idTime(self): return self.__idTime
  def get_senha(self): return self.__senha
  def get_idade(self): return self.__idade
  def get_nCamisa(self): return self.__nCamisa

  def set_id(self, id): 
    if isinstance(id, int):
      self.__id = id
    else:
      raise ValueError("Id invalido")
    
  def set_nome(self, nome): 
    if isinstance(nome, str):
      self.__nome = nome
    else:
      raise ValueError("O nome informado não é valido")
    
  def set_email(self, email): 
    if isinstance(email, str):
      self.__email = email
    else:
      raise ValueError("O e-mail informado não é valido")
    
  def set_idTime(self, idTime):
    if isinstance(idTime, int):
      self.__idTime = idTime
    else:
      raise ValueError("O id do time não é um número inteiro")

  def set_senha(self, senha):
    if isinstance(senha, int):
      self.__senha = senha
    else:
      raise ValueError("A senha informada não é composta apenas por números")
    
  def set_idade(self, idade):
    if isinstance(idade, int):
      self.__idade = idade
    else:
      raise ValueError("A idade informada não é valida")

  def set_nCamisa(self, nCamisa):
    if isinstance(nCamisa, int):
      self.__nCamisa = nCamisa
    else:
      raise ValueError("O numero de camisa não é valido")

  def __eq__(self, x):
    if self.__id == x.__id and self.__nome == x.__nome and self.__email == x.__email and self.__idTime == x.__idTime and self.__senha == x.__senha and self.__idade == x.__idade and self.__nCamisa == x.__nCamisa:
      return True
    return False

  def __str__(self):
    return f"{self.__id} - {self.__nome} - {self.__email} - {self.__idTime} - {self.__idade} - {self.__nCamisa}"
  
  def to_json(self):
    return {
      'Id': self.__id,
      'Nome': self.__nome,
      'E-mail': self.__email,
      'Id do Time': self.__idTime,
      'Senha': self.__senha,
      'Idade': self.__idade,
      'N da camisa': self.__nCamisa}


class NJogador(Modelo): 
  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("jogadores.json", mode="r") as arquivo:
        jogadores_json = json.load(arquivo)
        for obj in jogadores_json:
          aux = Jogador(obj["_Jogador__id"], 
                        obj["_Jogador__nome"], 
                        obj["_Jogador__email"],
                        obj["_Jogador__idTime"],
                        obj["_Jogador__senha"],
                        obj["_Jogador__idade"],
                        obj["_Jogador__nCamisa"])
          cls.objetos.append(aux)
    except FileNotFoundError:
      pass

  @classmethod
  def salvar(cls):
    with open("jogadores.json", mode="w") as arquivo:
      json.dump(cls.objetos, arquivo, default=vars)