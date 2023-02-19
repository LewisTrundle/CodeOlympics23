import * as THREE from "three";
import { WebGLRenderer } from "three";
import dogTexture from './salad_dog.png';

let x_direction = 1;
let y_direction = 1;
let z_direction = -1;


const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);

const text = document.getElementById("title");
console.log(text);
const renderer = new WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

const texture = new THREE.TextureLoader().load(dogTexture);
const geometry = new THREE.BoxGeometry( 5, 5, 5);
const material = new THREE.MeshBasicMaterial({ map: texture });
const cube = new THREE.Mesh(geometry, material);
scene.add(cube);
camera.position.z = 10;

setInterval(() => {
    //Generate a random colour
    console.log("COLOR INTERVAL");
    text.style.color = "#" + Math.floor(Math.random()*16777215).toString(16);
    console.log(text.style.color);
}, 1000);

function onWindowResize() {
    console.log("Window Resize");
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
  
    renderer.setSize(window.innerWidth, window.innerHeight);
}
  

window.addEventListener("resize", onWindowResize, false);

function animate() {
    requestAnimationFrame( animate );



    cube.rotation.x += 0.01;
    
    cube.rotation.z += 0.01;

    
    renderer.render(scene, camera);
}
animate();