
import { BrowserRouter, Routes, Route, RouteObject } from "react-router-dom";
import ComponentReact from './ComponentReactUrl';

const ComponentTypescriptRoutes = () => {

    const ComponentRoutes: RouteObject[] = [
        {
            path: "/ComponentTypescriptRoute",
            element: <ComponentReact />,
        },
    ];


    return <BrowserRouter>
        <Routes>
            {ComponentRoutes.map((route, index) => (
                <Route key={index} path={route.path} element={route.element} />
            ))}
        </Routes>
    </BrowserRouter>
}


export default ComponentTypescriptRoutes;