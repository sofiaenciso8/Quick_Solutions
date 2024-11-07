const parkingLot = document.getElementById('parking-lot');

const totalSlots = 24;
const slotsPerRow = 12;
const occupiedSlots = [10, 15, 28];
const prices = { 10: 35.0, 15: 35.0 };

for (let level = 1; level <= levels; level++) {
    const levelDiv = document.createElement('div');
    levelDiv.className = 'level';
    levelDiv.innerHTML = `<strong>Nivel ${level}:</strong>`;
    
for (let slot = 1; slot <= slotsPerLevel; slot++) {
    const slotNumber = (level - 1) * slotsPerLevel + slot;
    const slotDiv = document.createElement('div');
    slotDiv.className = 'slot';
    
    if (occupiedSlots.includes(slotNumber)) {
        slotDiv.classList.add('occupied');
    }
    
    const price = prices[slotNumber] || 0;
    if (price > 0) {
        const priceDiv = document.createElement('div');
        priceDiv.className = 'price';
        priceDiv.textContent = `$${price.toFixed(1)}`;
        slotDiv.appendChild(priceDiv);
    }
    
    slotDiv.innerHTML += `<div>${slotNumber}</div>`;
    levelDiv.appendChild(slotDiv);
  } parkingLot.appendChild(levelDiv);
}
