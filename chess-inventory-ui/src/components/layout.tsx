import Footer from "@/components/footer";
import {PropsWithChildren} from "react";
import Header from "@/components/header";

const MainLayout = ({children}: PropsWithChildren) => {
    return (
        <>
            <Header/>
            <main>{children}</main>
            <Footer/>
        </>
    );
};

export default MainLayout
