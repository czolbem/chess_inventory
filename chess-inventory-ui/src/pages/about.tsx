import {GetServerSideProps, InferGetServerSidePropsType, NextPage} from "next";

const About: NextPage = ({name}: InferGetServerSidePropsType<typeof getServerSideProps>) => {
return (
        <div>
            <h1>My name is: {name}</h1>
        </div>
    );
}
export const getServerSideProps: GetServerSideProps = async (context) => {
    const data = await fetch("https://randomuser.me/api").then((res) =>
        res.json()
    );

    return {
        props: {name: data.results[0].name.first},
    };
}

export default About