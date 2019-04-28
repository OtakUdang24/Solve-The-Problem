/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package soal_oop;

import java.util.Scanner;
import java.util.Map;
import java.util.HashMap;
import java.util.ArrayList;
/**
 *
 * @author User
 */
public class Input {
    String namaSiswa[];
    String mapel[];
    String data[][];
//    public Input(){
//        inputNama();
//        inputMapel();
//    }
    public void inputNama(){
        
        Scanner sc = new Scanner(System.in);
        System.out.println("Jumlah data: ");
        int inp = sc.nextInt();
        namaSiswa = new String[inp];
        for(int a=0;a < namaSiswa.length;a++){
            System.out.print("Nama murid ["+a+"] ");
            namaSiswa[a] = sc.next();
        }
    }
    
    public void inputMapel(){
        Scanner sc = new Scanner(System.in);
        System.out.println("Banyaknya Nilai yang diambil: ");
        int jumlah = sc.nextInt();
        mapel = new String[jumlah];
        for(int a=0;a < namaSiswa.length;a++){
            System.out.print("Penjelasan nama nilai ["+a+"] ");
            mapel[a] = sc.next();
        }
    }
    public void inputNilai(){
        
        
        int jumlahSiswa = namaSiswa.length;
        int jumlahMapel = mapel.length;
//        
        data = new String[jumlahSiswa][jumlahMapel];
//        for (int k=0;k < namaSiswa.length)
//        data[0][0] = 7;
//        System.out.print(data[0][0]);
    }
    
}
