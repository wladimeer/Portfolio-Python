const generateColors = () => {
  const labels = document.querySelectorAll('.technology');
  
  labels.forEach(({ style }) => {
    const redColor = generateRandomNumber({ max: 125, min: 20 });
    const greenColor = generateRandomNumber({ max: 152, min: 50 });
    const blueColor = generateRandomNumber({ max: 200, min: 20 });

    style.backgroundColor = `rgb(${redColor}, ${greenColor}, ${blueColor})`
  });
}

const generateRandomNumber = ({ max = 255, min = 50 }) => {
  return Math.floor(Math.random() * (max - min) + min);
}

document.addEventListener('DOMContentLoaded', function() {
  generateColors();
});