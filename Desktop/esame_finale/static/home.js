    
    document.getElementById('orderForm').onsubmit = async (e) => {
      e.preventDefault();
      alert("Ordine registrato!");
    };

    document.getElementById('corriereForm').onsubmit = async (e) => {
      e.preventDefault();
      alert("Corriere registrato!");
    };

    document.getElementById('statoOrdineForm').onsubmit = async (e) => {
      e.preventDefault();
      const codice = e.target.codice_spedizione.value;
      document.getElementById('statoOrdineResult').innerText = `Stato ordine ${codice} → In Transito`;
    };