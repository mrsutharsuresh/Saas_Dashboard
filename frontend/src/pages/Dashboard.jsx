import { useEffect, useState } from 'react';
import { useAuth } from '../context/AuthContext';
// import { PlusCircle } from 'lucide-react'; // Uncomment when icon lib is setup

export default function Dashboard() {
    const { user, logout, api } = useAuth();
    const [projects, setProjects] = useState([]);

    useEffect(() => {
        fetchProjects();
    }, []);

    const fetchProjects = async () => {
        try {
            const { data } = await api.get('/projects/');
            setProjects(data);
        } catch (error) {
            console.error("Failed to fetch projects", error);
        }
    };

    return (
        <div className="min-h-screen bg-gray-50">
            {/* Header */}
            <header className="bg-white shadow">
                <div className="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8 flex justify-between items-center">
                    <h1 className="text-3xl font-bold text-gray-900">My Dashboard</h1>
                    <button
                        onClick={logout}
                        className="text-gray-500 hover:text-gray-700 text-sm"
                    >
                        Logout ({user?.email})
                    </button>
                </div>
            </header>

            {/* Main Content */}
            <main>
                <div className="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">

                    {/* Action Bar */}
                    <div className="px-4 py-4 sm:px-0 flex justify-end">
                        <button className="bg-green-600 text-white px-4 py-2 rounded-lg shadow hover:bg-green-700 flex items-center">
                            {/* <PlusCircle className="w-5 h-5 mr-2" /> */}
                            + New Project
                        </button>
                    </div>

                    {/* Project Grid */}
                    <div className="px-4 py-4 sm:px-0">
                        {projects.length === 0 ? (
                            <div className="text-center py-20 bg-white rounded-lg border-2 border-dashed border-gray-300">
                                <p className="text-gray-500">No projects found. Create one!</p>
                            </div>
                        ) : (
                            <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3">
                                {projects.map((project) => (
                                    <div key={project.id} className="bg-white overflow-hidden shadow rounded-lg p-5">
                                        <h3 className="text-lg font-medium text-gray-900">{project.title}</h3>
                                        <p className="text-sm text-gray-500">Survey No: {project.survey_number || 'N/A'}</p>
                                        <div className="mt-4 flex justify-between items-center">
                                            <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-blue-100 text-blue-800">
                                                {project.status}
                                            </span>
                                            <button className="text-indigo-600 hover:text-indigo-900 text-sm">View</button>
                                        </div>
                                    </div>
                                ))}
                            </div>
                        )}
                    </div>

                </div>
            </main>
        </div>
    );
}
