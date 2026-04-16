import { useEffect } from "react"

import ProductDataRenderer from "./refactor-me/ProductDataRenderer"

function App() {
  useEffect(() => {
    new ProductDataRenderer().render()
  }, [])

  return (
    <div style={{ maxWidth: "600px" }}>
      <div id="nzdProducts"></div>
      <div id="usdProducts"></div>
      <div id="euProducts"></div>
    </div>
  )
}

export default App
