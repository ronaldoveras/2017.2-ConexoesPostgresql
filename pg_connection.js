const { Pool, Client } = require('pg')

const pool = new Pool({
  user: 'postgres',
  host: 'localhost',
  database: 'postgres',
  password: 'postgres',
  port: 5432,
})

pool.query('SELECT * FROM ESTACIONAMENTO WHERE CODIGOESTACIONAMENTO = $1', 
[2], (err, res) => {
  if(err){
    console.log(err.stack);
  } else {
    console.log('Código Estacionamento ' + res.rows[0].codigoestacionamento);  
    console.log('Código Veículo ' + res.rows[0].codigoveiculo);  
    console.log('Entrada Estacionamento ' + res.rows[0].dthoraentrada);  
    console.log('Saída Estacionamento ' + res.rows[0].drhorasaida);  
    
  }
  
});
pool.query('insert into estacionamento values ($1,$2, $3, $4)', [7, 2, '10/10/2017 08:48:16', '10/10/2017'], (err, res) => {
  if (err) {
    console.log("Erro");
    console.log(err.stack)
  } else {
    console.log("Sucesso");
  }
});

pool.end();

