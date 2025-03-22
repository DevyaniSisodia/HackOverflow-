import React, { useState, useEffect } from "react";
import axios from "axios";
import { 
    Container, Typography, TextField, Button, Card, CardContent, CircularProgress 
} from "@mui/material";
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from "recharts";

const API_BASE_URL = "http://127.0.0.1:8000";  // Update if FastAPI is hosted elsewhere

const App = () => {
    const [inventory, setInventory] = useState([]);
    const [formData, setFormData] = useState({ past_sales: "", seasonality: "", market_trends: "" });
    const [prediction, setPrediction] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState("");

    // Fetch inventory data on load
    useEffect(() => {
        axios.get(`${API_BASE_URL}/inventory/`)
            .then(response => setInventory(response.data))
            .catch(error => setError("Failed to fetch inventory data"));
    }, []);

    // Handle input changes
    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    // Send prediction request
    const handlePredict = async () => {
        setLoading(true);
        setError("");
        setPrediction(null);

        try {
            const response = await axios.post(`${API_BASE_URL}/predict/`, {
                past_sales: parseFloat(formData.past_sales),
                seasonality: parseFloat(formData.seasonality),
                market_trends: parseFloat(formData.market_trends),
            });

            setPrediction(response.data.predicted_demand);
        } catch (error) {
            setError("Error predicting demand. Check backend logs!");
        } finally {
            setLoading(false);
        }
    };

    return (
        <Container>
            <Typography variant="h4" gutterBottom>📊 Inventory Prediction Dashboard</Typography>

            <Card>
                <CardContent>
                    <Typography variant="h6">🔮 Predict Inventory Demand</Typography>
                    <TextField label="Past Sales" name="past_sales" value={formData.past_sales} onChange={handleChange} fullWidth />
                    <TextField label="Seasonality" name="seasonality" value={formData.seasonality} onChange={handleChange} fullWidth />
                    <TextField label="Market Trends" name="market_trends" value={formData.market_trends} onChange={handleChange} fullWidth />
                    
                    <Button 
                        variant="contained" 
                        color="primary" 
                        onClick={handlePredict}
                        disabled={loading}
                        style={{ marginTop: "10px" }}
                    >
                        {loading ? <CircularProgress size={24} /> : "Predict"}
                    </Button>

                    {error && <Typography color="error">{error}</Typography>}
                    {prediction !== null && <Typography variant="h6">📈 Predicted Demand: {prediction}</Typography>}
                </CardContent>
            </Card>

            <Typography variant="h6" style={{ marginTop: "20px" }}>📦 Inventory Data</Typography>
            {inventory.length > 0 ? (
                <ResponsiveContainer width="100%" height={300}>
                    <LineChart data={inventory}>
                        <CartesianGrid strokeDasharray="3 3" />
                        <XAxis dataKey="id" />
                        <YAxis />
                        <Tooltip />
                        <Legend />
                        <Line type="monotone" dataKey="past_sales" stroke="#8884d8" />
                        <Line type="monotone" dataKey="predicted_demand" stroke="#82ca9d" />
                    </LineChart>
                </ResponsiveContainer>
            ) : (
                <Typography>No inventory data available.</Typography>
            )}
        </Container>
    );
};

export default App;
