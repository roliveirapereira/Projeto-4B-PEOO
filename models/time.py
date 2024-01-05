import json
from models.modelo import Modelo

class Time:
  def __init__(self, id, nome, pontos):
    self.__id = id
    self.__nome = nome
    self.__pontos = pontos

  def get_id(self): return self.__id
  def get_nome(self): return self.__nome
  def get_pontos(self): return self.__pontos

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
    
  def set_pontos(self, pontos): 
    self.__pontos = pontos
    """ raise ValueError("A quantidade de pontos informada não é valida") """

  def __eq__(self, x):
    if self.__id == x.__id and self.__nome == x.__nome and self.__pontos == x.__pontos:
      return True
    return False

  def __str__(self):
    return f"{self.__id} - {self.__nome} - {self.__pontos}"
  
  def to_json(self):
    return {
      'Id': self.__id,
      'Nome': self.__nome,
      'Pontos': self.__pontos}
  
class NTime(Modelo):
  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("times.json", mode="r") as arquivo:
        times_json = json.load(arquivo)
        for obj in times_json:
          aux = Time(obj["Id"], 
                        obj["Nome"], 
                        obj["Pontos"])
          cls.objetos.append(aux)
    except FileNotFoundError:
      pass

  @classmethod
  def salvar(cls):
    with open("times.json", mode="w") as arquivo:
      json.dump(cls.objetos, arquivo, default=Time.to_json)