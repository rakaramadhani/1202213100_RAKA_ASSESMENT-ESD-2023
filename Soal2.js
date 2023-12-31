const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function cekPalindrom(kata) {
  // Menghapus spasi dan mengubah huruf menjadi huruf kecil
  const cleanedKata = kata.replace(/\s/g, '').toLowerCase();

  // Mengecek palindrom
  if (cleanedKata === cleanedKata.split('').reverse().join('')) {
    return "Eureeka!";
  } else {
    return "Suka blyat";
  }
}

// Menggunakan readline untuk mendapatkan input
rl.question("Masukkan kata atau kalimat: ", (inputKata) => {
  const hasilCek = cekPalindrom(inputKata);
  console.log(hasilCek);
  rl.close();
});
