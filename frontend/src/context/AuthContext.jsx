import { createContext, useState, useEffect, useContext } from 'react';
import axios from 'axios';
import { jwtDecode } from "jwt-decode";
import { useNavigate } from 'react-router-dom';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
    const [user, setUser] = useState(null);
    const [token, setToken] = useState(localStorage.getItem('token'));
    const [loading, setLoading] = useState(true);
    const navigate = useNavigate();

    // Axios instance with interceptor
    const api = axios.create({
        baseURL: 'http://localhost:8001', // Backend Port
    });

    api.interceptors.request.use((config) => {
        if (token) {
            config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
    });

    useEffect(() => {
        if (token) {
            try {
                const decoded = jwtDecode(token);
                // Check expiry
                if (decoded.exp * 1000 < Date.now()) {
                    logout();
                } else {
                    // Fetch user profile
                    fetchUser();
                }
            } catch (e) {
                logout();
            }
        }
        setLoading(false);
    }, [token]);

    const fetchUser = async () => {
        try {
            const { data } = await api.get('/users/me');
            setUser(data);
        } catch (error) {
            console.error("Fetch user failed", error);
            // logout(); // Optional: clean if api fails
        }
    };

    const login = async (email, password) => {
        try {
            // Note: Use x-www-form-urlencoded for OAuth2PasswordRequestForm
            const formData = new FormData();
            formData.append('username', email); // FastAPI expects 'username'
            formData.append('password', password);

            const { data } = await api.post('/auth/token', formData);
            localStorage.setItem('token', data.access_token);
            setToken(data.access_token);
            await fetchUser();
            navigate('/dashboard');
            return { success: true };
        } catch (error) {
            return { success: false, error: error.response?.data?.detail || "Login failed" };
        }
    };

    const logout = () => {
        localStorage.removeItem('token');
        setToken(null);
        setUser(null);
        navigate('/');
    };

    const value = {
        user,
        token,
        login,
        logout,
        loading,
        api
    };

    return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
};

export const useAuth = () => useContext(AuthContext);
