import { useState, useRef } from 'react'
import axios from 'axios'

function App() {
    const [description, setDescription] = useState('')
    const [loading, setLoading] = useState(false)
    const videoRef = useRef(null)
    const canvasRef = useRef(null)

    const startCamera = async () => {
        try {
            const stream = await navigator.mediaDevices.getUserMedia({ video: { facingMode: 'environment' } })
            if (videoRef.current) {
                videoRef.current.srcObject = stream
            }
        } catch (err) {
            console.error("Error accessing camera:", err)
        }
    }

    const captureAndAnalyze = async () => {
        if (!videoRef.current || !canvasRef.current) return

        const context = canvasRef.current.getContext('2d')
        canvasRef.current.width = videoRef.current.videoWidth
        canvasRef.current.height = videoRef.current.videoHeight
        context.drawImage(videoRef.current, 0, 0)

        canvasRef.current.toBlob(async (blob) => {
            if (!blob) return

            setLoading(true)
            const formData = new FormData()
            formData.append('file', blob, 'capture.jpg')

            try {
                // Use /api proxy configured in vite.config.js
                const response = await axios.post('/api/analyze', formData)
                const text = response.data.description
                setDescription(text)
                speak(text)
            } catch (err) {
                console.error("Error analyzing image:", err)
                setDescription("Error analyzing image.")
            } finally {
                setLoading(false)
            }
        }, 'image/jpeg')
    }

    const speak = (text) => {
        const utterance = new SpeechSynthesisUtterance(text)
        window.speechSynthesis.speak(utterance)
    }

    // Start camera on mount (or use useEffect)
    React.useEffect(() => {
        startCamera()
    }, [])

    return (
        <div className="container">
            <h1>VisuAlize</h1>
            <div className="camera-container">
                <video ref={videoRef} autoPlay playsInline muted style={{ width: '100%', maxHeight: '60vh', objectFit: 'cover' }} />
                <canvas ref={canvasRef} style={{ display: 'none' }} />
            </div>

            <div className="controls">
                <button onClick={captureAndAnalyze} disabled={loading} className="analyze-btn">
                    {loading ? 'Analyzing...' : 'Describe Environment'}
                </button>
            </div>

            {description && (
                <div className="result">
                    <p>{description}</p>
                </div>
            )}
        </div>
    )
}

export default App
