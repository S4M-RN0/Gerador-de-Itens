// Início dos botões
window.addEventListener('load', function() {
    document.getElementById ('btnNormal').addEventListener ('click', loot1);
    document.getElementById ('btnBoss').addEventListener ('click', loot2);
    document.getElementById ('btnMapa').addEventListener ('click', loot3);
    document.getElementById ('btnScroll').addEventListener ('click', loot4);
})
// Fim dos botões

// Início da função de botão de drop normal
function loot1() {
    limpaTela();
    eel.dropMenu(1, 0);
}
// Fim da função de botão de drop normal

// Início da função de botão de drop de boss
function loot2() {
    limpaTela();
    eel.dropMenu(2, 0);
}
// Fim da função de botão de drop normal

// Início das funções de botões drop de mapa
function loot3() {
    limpaTela();
    if (document.getElementById('mI').checked) {
        eel.dropMenu(3, 2);
    }
    else if (document.getElementById('mR').checked) {
        eel.dropMenu(3, 3);
    }
    else if (document.getElementById('mE').checked) {
        eel.dropMenu(3, 4);
    }
    else if (document.getElementById('mL').checked) {
        eel.dropMenu(3, 5);
    } 
}
// Fim das funções de botões de drop de mapa

// Início das funções de botões magia de pergaminho
function loot4() {
    limpaTela();
    if (document.getElementById('sC').checked) {
        eel.dropMenu(4, 1);
    }
    else if (document.getElementById('sI').checked) {
        eel.dropMenu(4, 2);
    }
    else if (document.getElementById('sR').checked) {
        eel.dropMenu(4, 3);
    }
    else if (document.getElementById('sE').checked) {
        eel.dropMenu(4, 4);
    }
    else if (document.getElementById('sL').checked) {
        eel.dropMenu(4, 5);
    } 
}
// Fim das funções de botões magia de pergaminho

// Início da função de imprimir na tela
eel.expose(printDrop);
function printDrop(item) {
    let display = document.getElementById('display');
    display.insertAdjacentHTML('beforeend', ('<p>'+item));
}

eel.expose(limpaTela);
function limpaTela() {
    let display = document.getElementById('display');
    display.innerHTML = '';
}
// Fim da função de imprimir na tela
