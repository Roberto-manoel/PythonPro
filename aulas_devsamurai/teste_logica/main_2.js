function trocarLampada() {
    subirEscada(20);
    retirarLampada();
    instalarNovaLampada();
    descerEscada(20);
    console.log("Lâmpada trocada com sucesso!");
  }
  
  function subirEscada(degraus) {
    if (escadaPosicionadaAbaixoDaLampada()) {
      for (let i = 0; i < degraus; i++) {
        subir();
      }
    } else {
      avisarOperador();
    }
  }
  
  function subir() {
    // implementação da lógica para subir um degrau da escada
  }
  
  function avisarOperador() {
    // implementação da lógica para avisar o operador
  }
  
  function retirarLampada() {
    // implementação da lógica para retirar a lâmpada
  }
  
  function instalarNovaLampada() {
    pegarNovaLampada();
    while (!lampadaEstaFixadaNoTerminal()) {
      girarSentidoHorario();
    }
  }
  
  function pegarNovaLampada() {
    // implementação da lógica para pegar uma nova lâmpada
  }
  
  function lampadaEstaFixadaNoTerminal() {
    // implementação da lógica para verificar se a lâmpada está fixada no terminal
  }
  
  function girarSentidoHorario() {
    // implementação da lógica para girar a lâmpada no sentido horário
  }
  
  function descerEscada(degraus) {
    for (let i = degraus; i > 0; i--) {
      descer();
      localizarLampada();
      testarLampada();
      if (lampadaQueimada()) {
        while (lampadaNoTerminal()) {
          girarSentidoAntiHorario();
          guardarLampadaNoRecipiente();
        }
        pegarNovaLampada();
      } else {
        avisarOperador();
      }
      while (!lampadaEstaFixadaNoTerminal()) {
        girarSentidoHorario();
      }
    }
  }
  
  function descer() {
    // implementação da lógica para descer um degrau da escada
  }
  
  function localizarLampada() {
    // implementação da lógica para localizar a lâmpada
  }
  
  function testarLampada() {
    // implementação da lógica para testar a lâmpada
  }
  
  function lampadaQueimada() {
    // implementação da lógica para verificar se a lâmpada está queimada
  }
  
  function lampadaNoTerminal() {
    // implementação da lógica para verificar se a lâmpada está no terminal
  }
  
  function girarSentidoAntiHorario() {
    // implementação da lógica para girar a lâmpada no sentido anti-horário
  }
  
  function guardarLampadaNoRecipiente() {
    // implementação da lógica para guardar a lâmpada no recipiente
  }
  
  function escadaPosicionadaAbaixoDaLampada() {
    // implementação da lógica para verificar se a escada está posicionada abaixo da lâmpada
  }