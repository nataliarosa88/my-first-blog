class Pessoa(object)
      nome=""
      endereco=""
      ano_nascimento=0

      def obter_idade(self)
          return 2016- self.ano_nascimento

class Funcionario(Pessoa)
        cargo=""
        salario=0

funcionario = Funcionario()
funcionario.nome='João Silva'
funcionario.ano_nascimento=1985
funcionario.endereco='Santa Maria'
funcionario.salario = 3000

print(funcionario.obter_idade())
