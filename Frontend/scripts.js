const URL ="http://127.0.0.1:5000/fila"

async function getProducts(){
    const resp = await fetch(URL);
    console.log(resp);
    if (resp.status === 200){
        const obj = await resp.json();
        obj.forEach(item => {
            console.log('Motor: ',item.motor);
            console.log('Lado: ',item.lado);
            console.log('Quantidade: ',item.quantidade);
            console.log('Status: ',item.status);
            
            
        });
    }
}

getProducts();

