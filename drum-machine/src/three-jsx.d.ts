declare global {
  namespace JSX {
    interface IntrinsicElements {
      // Three.js elements
      mesh: any
      boxGeometry: any
      circleGeometry: any
      meshStandardMaterial: any
      ambientLight: any
      pointLight: any
      color: any
    }
  }
}

export {}
