import React, { useState, useEffect } from "react";
import axios from "axios";

function Dashboard() {
    const [bots, setBots] = useState([]);

    useEffect(() => {
        axios.get("http://127.0.0.1:8000/api/configs/")
            .then((response) => setBots(response.data))
            .catch((error) => console.error(error));
    }, []);

    const handleRunBot = async (id) => {
        try {
            const response = await axios.post(`http://127.0.0.1:8000/api/configs/${id}/run/`);
            alert(response.data.result);
        } catch (error) {
            console.error(error);
        }
    };

    return (
        <div>
            <h1>Bot Dashboard</h1>
            {bots.map(bot => (
                <div key={bot.id}>
                    <h3>{bot.username}</h3>
                    <button onClick={() => handleRunBot(bot.id)}>Run Bot</button>
                </div>
            ))}
        </div>
    );
}

export default Dashboard;
