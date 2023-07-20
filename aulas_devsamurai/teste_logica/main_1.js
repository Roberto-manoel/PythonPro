let chiclete = {
  retiradoDoPlastico: false,
  mastigado: false,
  jogadoFora: false,
};

// Função para pegar o chiclete
function pegarChiclete() {
  if (!chiclete.retiradoDoPlastico) {
    chiclete.retiradoDoPlastico = true;
    console.log("Você pegou o chiclete.");
  } else {
    console.log("Você já pegou o chiclete.");
  }
}

// Função para mastigar o chiclete
function mastigarChiclete() {
  if (chiclete.retiradoDoPlastico) {
    if (!chiclete.mastigado) {
      chiclete.mastigado = true;
      console.log("Você mastigou o chiclete.");
    } else {
      console.log("Você já mastigou o chiclete.");
    }
  } else {
    console.log("Você precisa retirar o chiclete do plástico primeiro!");
  }
}

// Função para jogar o chiclete fora
function jogarChicleteFora() {
  if (chiclete.retiradoDoPlastico) {
    if (chiclete.mastigado) {
      if (!chiclete.jogadoFora) {
        chiclete.jogadoFora = true;
        console.log("O chiclete foi jogado fora.");
      } else {
        console.log("Você já jogou o chiclete fora.");
      }
    } else {
      console.log("Você precisa mastigar o chiclete primeiro!");
    }
} else {  
    console.log("Você precisa retirar o chiclete do plástico primeiro!");
  }
}

// Chama as funções para executar as ações
pegarChiclete();
mastigarChiclete();
jogarChicleteFora();