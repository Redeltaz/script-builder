import { Sidenav, Nav, Container, Sidebar } from "rsuite"
import Dashboard from "@rsuite/icons/Dashboard"
import './overlay.scss'

export const Overlay: React.FC = ({ children }) => {


    return <div className="overlay">
        <Container>
            <Sidebar collapsible style={{ display: 'flex', flexDirection: 'column' }}>
                <Sidenav style={{ height: "100%" }} expanded={true}>
                    <Sidenav.Body>
                        <Nav>
                            <Nav.Item eventKey="1" icon={<Dashboard />}>
                                Dashboard
                            </Nav.Item>
                        </Nav>
                    </Sidenav.Body>
                </Sidenav>
            </Sidebar>
            <Container>{children}</Container>
        </Container></div>
}