import Image from "next/image";
import Link from "next/link";
import React from "react";

function page() {
  return (
    <div className="overflow-x-hidden">
      <div className="flex-row w-xl md:flex bg-blue-100 md:w-5xl h-[600px] md:mt-28 md:ml-52 rounded-3xl ">
        <div className=" ">
          <Image
            width={600}
            height={400}
            className=" size-fit ml-8 mt-3 rounded-sm  md:ml-10 md:mt-11 md:rounded-4xl md:mb-6 "
            src="/signin.png"
            alt="image"
          ></Image>
        </div>
        <div className=" ml-6 mt-16 md:ml-40 md:mt-28">
          <h1 className=" ml-9 font-bold text-2xl">Welcome</h1>
          <h4 className="mt-12 text-lg">Username</h4>
          <input type="text" className="rounded-3xl bg-white h-10 w-56 mt-2" />
          <h4 className="mt-10 text-lg">Password</h4>
          <input
            type="password"
            className="rounded-3xl bg-white h-10 w-56 mt-2"
          />
          <br />
          <button className="bg-yellow-100 mt-8 text-lg w-32 rounded-lg h-10">
            SignIn
          </button>
          <Link href="/signup">
            <h5 className="text-sm mt-1">Dont have an account?Register</h5>
          </Link>
        </div>
      </div>
    </div>
  );
}

export default page;
